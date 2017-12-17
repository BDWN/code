
class StateService {

    constructor() {
        this.notifiers = [];
        this.xp = 2350;
    }

    subscribe(notifier) {
        this.notifiers.push(notifier)
    }

    getActivePost() {
        return this.activePostId || 0
    }

    setActivePost(id) {
        this.activePostId = id
        this.notifiers.forEach(x => x())
    }

    getXp() {
        return this.xp
    }

    setXp(val) {
        this.xp = val;
    }

}

export default new StateService();